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

    $("button#mag1").on('click', function(event) {
        $('#modal-1').fadeIn(500)
        $('#tag1').fadeOut(250)
        $('img#1').fadeOut(500)
        setTimeout(function(){
            document.querySelector('#modal-1').style.display = 'flex';
        }, 500);
    });
    $("button.modal-button").on('click', function(event) {
        $('#modal-1').fadeOut(500)
        $('#tag1').fadeIn(250)
        $('img#1').fadeIn(500)
        setTimeout(function(){
            document.querySelector('#modal-1').style.display = 'none';
        }, 500);
    });
    $("button#mag2").on('click', function(event) {
        $('#modal-2').fadeIn(500)
        $('#tag2').fadeOut(250)
        $('#mag2').fadeOut(250)
        $('.r2').fadeOut(250)
        $('img#2').fadeOut(500)
        setTimeout(function(){
            document.querySelector('#modal-2').style.display = 'flex';
        }, 500);
    });
    $("button.modal-button").on('click', function(event) {
        $('#modal-2').fadeOut(500)
        $('#tag2').fadeIn(250)
        $('#mag2').fadeIn(250)
        $('.r2').fadeIn(250)
        $('img#2').fadeIn(500)
        setTimeout(function(){
            document.querySelector('#modal-2').style.display = 'none';
        }, 500);
    });
});
