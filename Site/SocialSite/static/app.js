var nitification = document.querySelector('.not_mess img:nth-child(1)');
var hidden_nav = document.querySelector('.hidden_div');
var messages = document.querySelector('.sen');
var hidden_nav_message = document.querySelector('.hidden_div_message');
var post_btn = document.querySelectorAll('.post_top button');
var hidden_option = document.querySelector('.hidden_option');
var post = document.querySelector('.post_top');


nitification.addEventListener('click', function(){
    if( hidden_nav.style.display == 'none'){
        hidden_nav.style.display = 'block';
    }
    
    else{
        hidden_nav.style.display = 'none';
    }
});



messages.addEventListener('click', function(){
    if( hidden_nav_message.style.display == 'none'){
        hidden_nav_message.style.display = 'block';
    }
    
    else{
        hidden_nav_message.style.display = 'none';
    }
});



/*post btn*/

for(var i = 0; i < post_btn.length; i++){
    post_btn[i].addEventListener('click', function(ev){
        var target = ev.target.parentElement.nextElementSibling;
        if(target.style.display == 'none'){
            target.style.display = 'block'
        }else{
            target.style.display = 'none'
        }
})
}



/*profile Button*/
var profile = document.querySelector('.profile_dev');
var hiddenProfile = document.querySelector('.hidden_profile');

profile.addEventListener('click', function(){
    if( hiddenProfile.style.display == 'none'){
        hiddenProfile.style.display = 'block';
    }
    
    else{
        hiddenProfile.style.display = 'none';
    }
});





















