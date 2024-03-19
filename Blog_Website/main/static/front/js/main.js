$(document).ready(function () {
  $(function () {
    AOS.init({
      once: true,
      offset: 10,
    });
  });

  $(".banner-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 450,
    nav: true,
    loop: true,
    dots: false,
    mouseDrag: false,
    touchDrag: false,
    margin: 1,

    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
      },
    },
  });

  $(".menu").click(function () {
    $(".pages").toggleClass("active");
  });

  const toUp = document.querySelector(".scrollup");
  window.addEventListener("scroll", () => {
    if (window.pageYOffset > 1000) {
      toUp.classList.add("active");
    } else {
      toUp.classList.remove("active");
    }
  });

  $(".scrollup").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1000);
  });

  $(".textarea").on("input", function () {
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
  });

  $(".reply-btn").on("click", function () {
    if ($(this).html() == "پاسخ") $(this).html("انصراف از پاسخ");
    else if ($(this).html("انصراف از پاسخ")) $(this).html("پاسخ");

    $(this)
      .parent()
      .parent()
      .parent()
      .next(".reply-form")
      .slideToggle("slow", function () {
        $(".reply textarea").focus();
      });
  });

  $(".see-replies").on("click", function () {
    $(this)
      .parent()
      .parent()
      .parent()
      .next()
      .next(".reply")
      .slideToggle("slow");

    var text = $(this).html();
    if (text.includes("مشاهده")) {
      var replacement = $(this).html().replace("مشاهده", "مخفی کردن");

      $(this).html(replacement);
    } else {
      var text = $(this).html().replace("مخفی کردن", "مشاهده");
      $(this).html(text);
    }
  });

  $(".small-categories").on("click", function () {
    $(".small-dropdown").not($(this).next()).slideUp();
    $(".small-categories i")
      .not($("i", this))
      .addClass("fa-chevron-down")
      .removeClass("fa-chevron-up");
    $(this).next(".small-dropdown").slideToggle();
    $("i", this).toggleClass("fa-chevron-up fa-chevron-down");
  });

  $(".toggle i").on("click", function () {
    $(".small").toggleClass("active");
    $(this).toggleClass("fa-times fa-bars");
  });

  $(document).on("click", function () {
    $(".simple-search").slideUp();
  });

  $(".search-button i").on("click", function (event) {
    event.stopPropagation();
    $(".simple-search").slideToggle(300);
  });

  $(".simple-search").on("click", function (event) {
    event.stopPropagation();
  });

  setTimeout(function () {
    $("#message").fadeOut("slow");
  }, 2500);
});
