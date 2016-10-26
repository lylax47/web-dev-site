$(document).ready(function(){
    $('#colls').dynatable ({
        dataset: {
        PerPageDefault: 10,
        perPageOptions:[10],
        },
          table: {
            defaultColumnIdStyle: 'camelCase',
            columns:  null,
            headRowClass: null
        }
    });
    $('#settings, #instruct, .page-header, th').hover(
        function(){
            $(this).fadeTo("fast", 1);
        },

        function(){
            $(this).fadeTo("fast", 0.7);
        }
    );
    $('td').hover(
        function(){
            $(this).fadeTo("fast", 1);
            $(this).css('background', '#F1DC96');
        },

        function(){
            $(this).fadeTo("fast", 0.7);
            $(this).css('background', '#fff');
        }
    );
});