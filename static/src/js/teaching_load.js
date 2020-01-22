$(document).ready(function(){
    var td = $("#time_schedule table tr");
    td.selectable({
          create: function( event, ui ) {
          }
    });

    td.on( "selectablecreate", function( event, ui ) {
    } );

    td.selectable({
      selected: function( event, ui ) {
          var selected_time = $(this).closest('.time-row').find("td:first").text();
          $(this).closest('table').find("tr td").removeClass("selected-time")
          get_time()
      }
    });
})
var date_time_list= [];

function save_class_schedule(){
    csrf_token = "<t t-esc='request.csrf_token(None)'/>";
    var classes_id = $('table#time_schedule').attr("classes-id");
    $.ajax({
        url:'/class/form_view/schedule/save/',
        type:'POST',
        contentType: "application/json",
        data: JSON.stringify({params:{date_time_list, 'classes_id':classes_id}}),
        success:function(data){
            location.reload();
        },
        error:function(){
            alert("success")
        }
    })
}

function get_time(){
      date_time_list=[];
      $(".day-label").each(function(index){
        var day_selected = $(this).attr("name");
        var time_list = []

        $('.time-row').each(function(row_index){
            var cell_selected = $(this).find(".time td:eq("+index+")");
            var time_selected = $(this).find("td:first").attr("name");
            if(cell_selected.hasClass("ui-selected")){
                time_list=time_selected;
                date_time_list.push({day: day_selected, time: time_list})
            }
        });
      });
      console.log(date_time_list)
}