$(document).ready(updateCards);

$('button').click(updateCards);

$('.cards-table').on('click', 'img', function(){
  $('h4').text('');
  if ($('.selected').length >= 3) {
    if ($(this).hasClass('selected')) {
      $(this).toggleClass('selected');
    }
  }
  else {
    $(this).toggleClass('selected');
  }

  if ($('.selected').length == 3) {
    var selectedCards = []
    $('.selected').each( function(index) {
      selectedCards.push($(this).data('dict'));
    });
    selected(selectedCards);
  }
});

function updateCards(){
  $('h4').text('');
  $('.cards-table').html('').load('/setgame/update-cards/');
}

function selected(selectedCards){
  $.ajax({
    url: '/setgame/selected/',
    method: 'POST',
    data: {
      'selectedCards':  JSON.stringify(selectedCards)
    },
    success: function(data) {
      $('h4').text(data)
    }
  });
}
