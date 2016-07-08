using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;
using Moq;
using Ninject;
using Store.Domain.Abstract;
using Store.Domain.Concrete;
using Store.Domain.Entities;

namespace Store.WebUI.Infrastructure
{
    public class NinjectControllerFactory:DefaultControllerFactory
    {
        private readonly IKernel _ninjectKernel;

        public NinjectControllerFactory()
        {
            this._ninjectKernel = new StandardKernel();
            AddBindings();
        }

        private void AddBindings()
        {
            //var mock = new Mock<IProductRepository>();
            //mock.Setup(m => m.Products)
            //    .Returns(new List<Product> { new Product() { Name = "Football", Price = 25 }, new Product() { Name = "Base", Price = 125 } }.AsQueryable());
            //_ninjectKernel.Bind<IProductRepository>().ToConstant(mock.Object);
            _ninjectKernel.Bind<IProductRepository>().To<EFProductRepository>();
        }

        protected override IController GetControllerInstance(RequestContext requestContext, Type controllerType)
        {
            return controllerType == null ? null : (IController) _ninjectKernel.Get(controllerType);
        }
    }
}