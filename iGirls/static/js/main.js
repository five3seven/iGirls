$(document).ready(function() {

    $("form.b1").on('submit', function(event) {

        var player1 = $(".btn1").val();
        var player2 = $(".btn2").val();

        $.ajax({
            url : "/vote",
            type : "POST",
            data : { "winner" : "1", "player1" : player1, "player2" : player2 },
            cache : false,
            success : function(data) {
                $("#container").fadeOut(500)
                setTimeout(function(){
                    $("#container").replaceWith(data);
                }, 500);
            }
        });
        event.preventDefault();
    });

    $("form.b2").on('submit', function(event) {

        var player1 = $(".btn1").val();
        var player2 = $(".btn2").val();

        $.ajax({
            url : "/vote",
            type : "POST",
            data : { "winner" : "2", "player1" : player1, "player2" : player2 },
            cache : false,
            success : function(data) {
                $("#container").fadeOut(500)
                setTimeout(function(){
                    $("#container").replaceWith(data);
                }, 500);
            }
        });
        event.preventDefault();
    });

    $("form.r1").on('submit', function(event) {

        var player = $(".btn1").val();

        $.ajax({
            url : "/report",
            type : "POST",
            data : { "report" : player },
            cache : false,
            success : function(data) {
                $("#container").fadeOut(500)
                setTimeout(function(){
                    $("#container").replaceWith(data);
                }, 500);
            }
        });
        event.preventDefault();
    });

    $("form.r2").on('submit', function(event) {

        var player = $(".btn2").val();

        $.ajax({
            url : "/report",
            type : "POST",
            data : { "report" : player },
            cache : false,
            success : function(data) {
                $("#container").fadeOut(500)
                setTimeout(function(){
                    $("#container").replaceWith(data);
                }, 500);
            }
        });
        event.preventDefault();
    });

    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
    console.log(vh)

    $("form.m1").on('submit', function(event) {
        console.log(11)
        document.querySelector('.bg-modal').style.display = 'flex';
    });
});
