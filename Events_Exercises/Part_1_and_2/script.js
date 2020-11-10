// Part 1
    	document.addEventListener('DOMContentLoaded', function() {
    		document.querySelector('#change_heading').innerText = 'Hello World!';

    		let section = document.querySelector('section');
    		let selected = document.querySelector('.selected');
    		section.addEventListener('mouseover', function(e) {
    			selected.innerText = e.target.className
    		})

    		let newDiv = document.createElement('div');
    		newDiv.classList.add('purple');
    		newDiv.style.backgroundColor = 'purple';

    		section.append(newDiv)

    		// Part 2
    		let button = document.querySelector('button');
    		let car1 = document.querySelector('.car1');
    		let car2 = document.querySelector('.car2');

    		button.addEventListener('click', function() {
    			startRace(car1, car2)
    		});

    		function startRace(a, b) {
    			button.disabled = true
    			let aPosition = 0
    			let bPosition = 0
    			
    			a.timer = setInterval(function() {
    				
    				if ( aPosition > 1300) {
    					alert('Car 1 Wins!')
    					resetCarRace(a, b)
    				} else {
						aPosition = aPosition +  Math.random()*100 ;
						a.style.left = parseInt(aPosition) + 'px';
    				}
    			}, 30)

    			b.timer = setInterval(function() {
    				
    				if ( bPosition > 1300) {
    					alert('Car 2 Wins!')
    					resetCarRace(a, b)
    				} else {
						bPosition = bPosition +  Math.random()*100 ;
						b.style.left = parseInt(bPosition) + 'px';
    				}
    			}, 30)
    		}

    		function resetCarRace(a, b) {
    				clearInterval(a.timer)
    				clearInterval(b.timer)
    				a.style.left = 0 + 'px'
    				b.style.left = 0 + 'px'
	    			button.disabled = false
    		}
    		
    	})