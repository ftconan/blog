// $ is not a function
// 用jQuery 替换 $
jQuery(function(){
    // 将blog内容html化
    var blogContent = jQuery("#blogContent").text();
    jQuery("#blogContent").html(blogContent);
});
