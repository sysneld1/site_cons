<script>
$(function() { 
  $('[data-toggle="tab"]').on('shown.bs.tab', function () {
    // сохраним последнюю вкладку      
    localStorage.setItem('lastTab', $(this).attr('href'));
  });
  //перейти к последней вкладки, если она существует:
  var lastTab = localStorage.getItem('lastTab');
  if (lastTab) {
    $('[href="' + lastTab + '"]').tab('show');
  }
  else
  {
    // установить первую вкладку активной если lasttab не существует
    $('[data-toggle="tab"]:first').tab('show');
  }
});
</script>