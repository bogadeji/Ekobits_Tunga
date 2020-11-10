```<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div class="header">
    </div>
    <section id="container">
        <ul>
            <li class="first">one</li>
            <li class="second">two</li>
            <li class="third">three</li>
        </ul>
        <ol>
            <li class="first">one</li>
            <li class="second">two</li>
            <li class="third">three</li>
        </ol>
    </section>
    <div class="footer">
    </div>
</body>
</html>
```

1. `document.getElementById('container')`

2. `document.querySelector('#container')`

3. `document.querySelectorAll('.second')`

4. `document.querySelectorAll('ol .third')`

5. `document.querySelector('#container').innerText = 'Hello!'`

6. `document.querySelector('.footer').classList.add('main')`

7. `document.querySelector('.footer').classList.remove('main')`

8. `let list = document.createElement('li')`

9. `list.innerText = 'four'`

10. ```let ul = document.querySelector('ul')
ul.appendElement(list)
```

11. ``` let lis = document.querySelectorAll('ol li')
for(let i=0; i<lis.length; i++) {
	lis[i].style.backgroundColor = 'green'
}
```

12. `document.querySelector('.footer')remove()`


