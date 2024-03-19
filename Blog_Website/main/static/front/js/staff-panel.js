$(document).ready(function () {
  $(".sidebar-btn").click(function () {
    $(".wrapper").toggleClass("sidebar-collapse");
  });

  $(".menu-btn").click(function () {
    $(this).next(".sub-menu").slideToggle();
    $(".sidebar").animate(
      {
        scrollTop: $(this).next(".sub-menu").offset().top - 70,
      },
      1500
    );
  });

  $("#category-selector").on("change", function (e) {
    let selector = $(this).val();
    $("#subcategory-selector ").prop("selectedIndex", 0);
    $("#subcategory-selector > option").hide();
    $("#subcategory-selector > option")
      .filter(function () {
        return $(this).data("pub") == selector;
      })
      .show();
  });

  $("#subcategory-selector").on("change", function (e) {
    let selector = $("option:selected", this).data("pub");
    $("#category-selector").val(selector);
  });

  tinymce.init({
    selector: ".body-text",
    toolbar:
      "a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table",
    toolbar_mode: "floating",
    tinycomments_mode: "embedded",
    plugins:
      "autoresize print preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons",
    init_instance_callback: function (editor) {
      var freeTiny = document.querySelector(".mce-notification");
      freeTiny.style.display = "none";
    },
  });

  $(".reply-btn").on("click", function () {
    $(this)
      .next(".reply-form")
      .slideToggle(function () {
        $("textarea", this).focus();
        $(this).prev().toggleClass("change");
        if ($(this).prev().html() == "پاسخ") $(this).prev().html(" لغو ");
        else if ($(this).prev().html() == "نمایش پاسخ")
          $(this).prev().html("مخفی کردن پاسخ");
        else if ($(this).prev().html() == "مخفی کردن پاسخ")
          $(this).prev().html("نمایش پاسخ");
        else if ($(this).prev().html() == "لغو") $(this).prev().html("پاسخ");
      });
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
});
