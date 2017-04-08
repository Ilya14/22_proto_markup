function setRegion(region)
{
  var selectedString = $(region).text();
  $('.navbar').find('.popover-bottom').html('Регион: ' + selectedString + '<b class="caret"></b>');
  $('.jumbotron').find('.dropdown-toggle').html('в ' + selectedString + '<span class="caret"></span>');
  $('.table').find("[style='text-align:right;']").find('.dropdown-toggle').html(selectedString + '<span class="caret"></span>');
  $('.modal').modal('hide');
}

function onRegionOk()
{
  setRegion($('.popover').find('b'));
  $('.popover').remove();
}

function onRegionNo()
{
  $('.popover').remove();
}