//解决Django ajax post请求 csrf 拦截
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = $("input[name='csrfmiddlewaretoken']").val();
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
(function (a) {
    a(window).on("load", function () {
        a("#loading").fadeOut();
        a("#loading").delay(350).fadeOut("slow")
    });
    a('a[href^="#"]').on("click", function (d) {
        var c = a(this);
        a("html, body").stop().animate({scrollTop: a(c.attr("href")).offset().top}, 1000);
        d.preventDefault()
    });
    a("#scroll-up").on("click", function (c) {
        c.preventDefault();
        a("html, body").animate({scrollTop: 0}, 1000)
    });
    a(window).on("scroll", function () {
        if (a(this).scrollTop() > 100) {
            a(".scroll-up").fadeIn()
        } else {
            a(".scroll-up").fadeOut()
        }
    });
    a(".header").sticky({topSpacing: 0});
    a("body").scrollspy({target: ".navbar-custom", offset: 70});
    a(".js-height-full").height(a(window).height());
    a(window).resize(function () {
        a(".js-height-full").height(a(window).height())
    });
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
        a("#home").css({"background-attachment": "scroll"})
    } else {
        a("#home").parallax("50%", 0.1)
    }
    a(".testimonials").owlCarousel({
        singleItem: true,
        navigation: false,
        pagination: true,
        slideSpeed: 300,
        paginationSpeed: 400,
        autoPlay: 5000,
        navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>']
    });
    var b = a(".list-items-container");
    a("#filter li").on("click", function (c) {
        c.preventDefault();
        a("#filter li").removeClass("active");
        a(this).addClass("active");
        var d = a(this).attr("data-group");
        var f = a(this).attr("data-group");
        b.shuffle("shuffle", f)
    });
    a(document).ready(function () {
        a(".simple-ajax-popup").magnificPopup({type: "image", gallery: {enabled: true}})
    });
    new WOW().init();
    a("body").fitVids()
})(jQuery);