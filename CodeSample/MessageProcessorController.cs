using System.Collections.Generic;
using NLog;
using Processor.Abstract;
using Processor.Converters;
using Processor.Exceptions;
using Processor.Model;
using MailService.Contracts;
using System;


namespace Processor
{
    /// <summary>
    /// класс обработки заявок. Обеспечивает постоянную обработку заявок и отправку ответа клиенту
	///При появлении заявки в очереди вызывается метод интерфейса Process
    /// </summary>
    public class MessageProcessorController:IProcessor
    {
        private static readonly Logger Log = LogManager.GetLogger();
		//Реализованные интерфейсами параметры можно задавать через DI и тестирование отдельных компонент
        private readonly IMailService _mailService;//Произваодит отправку результатов работы клиенту
        private readonly IMessageProcessor _messageProcessor;//Производит обработку запросов   
		private readonly Mailer _mailer; //Хранит тексты сообщений
        
		//Возможна асинхронное отслеживание ошибок
		public event Action<RequestModel> MessageProcessingFailed;//Событие при ошибке обработки сообщения
        public event Action<RequestModel> MessageValidation;//Событие при ошибке валидации
        
		/// <summary>
        /// Конструктор
        /// </summary>
        /// <param name="messageProcessor">класс обработчик</param>
		/// <param name="mailService">сервис возвращающий ответы клиенту</param>
		/// <param name="mailer">объект формирующий сообщения для пользователя</param>
        public MessageProcessorController(IPageParser messageProcessor, IMailService mailService, Mailer mailer)
        {
			
			_messageProcessor = messageProcessor;
            _mailService = mailService;
			_mailer = mailer;
        }

        /// <summary>
        /// обработка одной заявки, находящейся в очереди в формате json
        /// </summary>
        /// <param name="request">Объект десериализованный из json</param>
        public void Process(RequestModel requestModel)
        {
            if (requestModel == null)
            {
                Log.Error("Поступившая заявка null");
                return;
            }
            try
            {
                var request = new RequestConverter(requestModel);//определение типа заявки и ее форматирование в типизированный  
                var mail = _messageProcessor.Process(request);//вызов метода от Process в зависимости от определенного типа
                _mailService.SendMail(mail);//Отправка отчета клиенту
                Log.Info("Id: {0} Сообщение отправлено клиенту", request.Id);//Заявка успешно обработана
            }			
            catch (InputValidationException ive)//ошибочная ситуация - тип заявки не определен
            {
                if (MessageValidation != null)
                {
                    MessageValidation(requestModel);
                }
                _mailService.SendMail(_mailer.CreateValidationMessage(requestModel, ive.Message));
                Log.Info("Id: {0} Сообщение о ошибке валидации отправлено клиенту. Ошибка {1}", requestModel.Id,
                    ive.Message);
            }			
            catch (MailIsNotValidException ex)//критическая ошибка, обработать заявку не удалось
            {
                if (MessageProcessingFailed != null)
                {
                    MessageProcessingFailed(requestModel);
                }
                Log.Error(string.Format("Id: {0} Возникла критическая ошибка: {1}", requestModel.Id, ex.Message), ex);
            }
        }
    }

}
