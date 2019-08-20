 /* # = class 
    . id
    Author Nino felino
 */
 $('#add').click(function(){
      alert('click #add'); 
    });
    $('.add').click(function(){
      console.info("monitor");
      alert(self.href); 
      
    });
$('#del').click(function(){alert('click #delete'); });
$('.del').click(function(){alert('click .delete'); });
$('.add').click(function(){console.info("monitor");alert(self.href); });
