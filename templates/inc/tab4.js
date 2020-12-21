$(function(){
  // nav - id контейнера, содержащего вкладки
  var nav = $('#nav');
  nav.find('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    nav.find('.dropdown a[href="'+$(e.target).attr('href')+'"]').triggerHandler('click',[true]);
  });
  nav.find('.dropdown a').click(function(e,show){
    e.preventDefault();
    if (!show) {
      $(nav.find('a[href="'+$(this).attr('href')+'"]')).tab('show');
    }
    $(this).closest('ul').find('li').removeClass('disabled active');
    $(this).parent().addClass('disabled');
    $(this).closest('.dropdown').find('button').html($(this).text() + ' <span class="caret"></span>');
  });
  
  nav.find('.dropdown a[href="'+$('#navtab li.active a').attr('href')+'"]').triggerHandler('click',[true]);

});