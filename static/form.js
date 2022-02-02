
const myTimeout = setTimeout(stopGame, 60000);

function stopGame() {
    $(document).ready(function() {
        $('form').submit(function(e) {
            e.preventDefault();
            $("#btn_submit").attr("disabled", true);
        });
    });
} 

 $(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : {
                
                word : $('#word').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(JSON.stringify(data.error)).show();
                $('#successAlert').hide();
                $('#worningAlert').hide();
            }
            else if(data.word) {
                $('#successAlert').text(JSON.stringify(data.word),data.score).show();
                $('#errorAlert').hide();
                $('#worningAlert').hide();
            }
            else
            {
                $('#worningAlert').text(JSON.stringify(data.worning)).show();
                $('#errorAlert').hide();
                $('#successAlert').hide();
            }
        });
        event.preventDefault();
    });
});
 