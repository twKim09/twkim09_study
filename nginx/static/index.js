function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }



    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

var csrf_token = '<%= token_value %>';


$(document).ready(function(){
    $("#btnOK").click(function(){
        $("#showData").empty();
            $.ajax({
                url:'/api/mysql/',
                type:'get',
                dataType:'json',
                success:function(data){
                    $("#showData").html(data);},
                error:function(){
                    $("#showData").text("error");
                }
                });
            });
        });

$(document).ready(function(){
    $("#btnProd").click(function(){
        $("#ProdReturn").empty();

        var message = document.getElementById("kafka-prod").value;
        console.log(message)
            $.ajax({
                url:'/api/producer/',
                type:'post',
                dataType:'json',
                data: JSON.stringify({"kafka-prod":message}),
                success:function(data){
                    $("#ProdReturn").html(data);},
                error:function(){
                    $("#ProdReturn").text("error");
                }
                });
            });
        });

$(document).ready(function(){
    $("#dbinput").click(function(){


        var name = document.getElementById("name").value;
        var password = document.getElementById("password").value;
        console.log(name);

        $.ajax({
            url:'/api/dbinput/',
            type:'post',
            dataType:'json',
            data: JSON.stringify({"name":name,"password":password}),

            success:function(data){
                alert(data);
            },
            error:function(){
                alert("error");
            }
        });
    });
});

$(document).ready(function(){
    $("#getdata").click(function(){


        $.ajax({
            url:'http://13.113.240.145/api/mysql/',
            type:'get',
            dataType:'json',
            success:function(data){
                $("#showData2").html(data);
            },
            error:function(){
                alert("Error");
            }
        });
    });
});
$(document).ready(function(){
    $("#kafka-consumer-btn").click(function(){
        $("#kafka-consumer").empty();


        $.ajax({
            url:'/api/consumer/',
            type:'get',
            dataType:'json',
            success:function(data){
                $("#kafka-consumer").html(data);
            },
            error:function(){
                $("#kafka-consumer").text("error");
            }
        });
    });
});
