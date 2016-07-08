using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Store.Domain.Abstract;

namespace Store.WebUI.Controllers
{
    public class ProductController : Controller
    {
        private IProductRepository _repository;

        public int PageSize = 1;

        

        public ProductController(IProductRepository productRepository)
        {
            _repository = productRepository;
        }

        public ViewResult List(int page = 1)
        {
            return View(_repository.Products
                .OrderBy(p=>p.ProductId)
                .Skip((page-1)*PageSize)
                .Take(PageSize));
        }
    }
}
