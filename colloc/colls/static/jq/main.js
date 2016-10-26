$(document).ready(function(){
    $('#colls').dynatable ({
        features: {
            perPageSelect:null,
        },
          table: {
            defaultColumnIdStyle: 'camelCase',
            columns:  null,
            headRowClass: null
        }
    });
});