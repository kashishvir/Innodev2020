for (var i=0;i<document.querySelectorAll(".alpha").length;i++)
//for {var i=0;i<numberOfDrumButtons;i++}
{document.querySelectorAll(".alpha")[i].addEventListener("click",function()
{
    var buttonInnerHTML=this.innerHTML;
    makeSound(buttonInnerHTML);
    buttonAnimation(buttonInnerHTML);
});
}


document.addEventListener("keypress",function(event)
{ makeSound(event.key);
  buttonAnimation(event.key);
});

function makeSound(key)
{
  switch (key)
  {
          case "A": var audio1 = new Audio("MUSIC/a.mp3");
                        audio1.play();
                        break;
          case "B": var audio2 = new Audio("MUSIC/b.mp3");
                        audio2.play();
                        break;
          case "C": var audio3 = new Audio("MUSIC/c.mp3");
                        audio3.play();
                        break;
          case "D": var audio4 = new Audio("MUSIC/d.mp3");
                        audio4.play();
                        break;
          case "E": var audio5 = new Audio("MUSIC/e.mp3");
                        audio5.play();
                        break;
          case "F": var audio6= new Audio("MUSIC/f.mp3");
                        audio6.play();
                        break;
          case "G": var audio7= new Audio("MUSIC/g.mp3");
                        audio7.play();
                        break;
          case "H": var audio8= new Audio("MUSIC/h.mp3");
                        audio8.play();
                        break;
          case "I": var audio9= new Audio("MUSIC/i.mp3");
                        audio9.play();
                        break;
          case "J": var audio10= new Audio("MUSIC/j.mp3");
                        audio10.play();
                        break;
          case "K": var audio11= new Audio("MUSIC/k.mp3");
                        audio11.play();
                        break;
          case "L": var audio12= new Audio("MUSIC/l.mp3");
                        audio12.play();
                        break;
          case "M": var audio13= new Audio("MUSIC/m.mp3");
                        audio13.play();
                        break;
          case "N": var audio14= new Audio("MUSIC/n.mp3");
                        audio14.play();
                        break;
          case "O": var audio15= new Audio("MUSIC/o.mp3");
                        audio15.play();
                        break;
          case "P": var audio16= new Audio("MUSIC/p.mp3");
                        audio16.play();
                        break;
          case "Q": var audio17= new Audio("MUSIC/q.mp3");
                        audio17.play();
                        break;
          case "R": var audio18= new Audio("MUSIC/r.mp3");
                        audio18.play();
                        break;
          case "S": var audio19= new Audio("MUSIC/s.mp3");
                        audio19.play();
                        break;
          case "T": var audio20= new Audio("MUSIC/t.mp3");
                        audio20.play();
                        break;
          case "U": var audio21= new Audio("MUSIC/u.mp3");
                        audio21.play();
                        break;
          case "V": var audio22= new Audio("MUSIC/v.mp3");
                        audio22.play();
                        break;
          case "W": var audio23= new Audio("MUSIC/w.mp3");
                        audio23.play();
                       break;
          case "X": var audio24= new Audio("MUSIC/x.mp3");
                        audio24.play();
                        break;
          case "Y": var audio25= new Audio("MUSIC/y.mp3");
                        audio25.play();
                        break;
          case "Z": var audio26= new Audio("MUSIC/z.mp3");
                        audio26.play();
                        break;
          default: console.log(buttonInnerHTML);

        }
}
function buttonAnimation(currentKey){
  var activeButton=document.querySelector("."+currentKey);
  activeButton.classList.add("pressed");
  setTimeout(function(){
    activeButton.classList.remove("pressed");
  },100);
}
