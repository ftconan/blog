$(function(){
    $.post("getUserName",function(data){          //传给getUserName
        var str=data;
        $("#userName").append(str);
    })
})