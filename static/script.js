if (!localStorage.getItem('counter'))
{
    localStorage.setItem('counter', 1)
}



function chnge_theme()
{
    let counter = localStorage.getItem('counter')
    theme = document.getElementById("main")
    filters = document.getElementById("theme")
    tasks = document.getElementById("theme1")
    todo = document.getElementById("todo-input")
    add = document.getElementById("add")


    if (counter % 2 == 1)
    {
        theme.style.backgroundImage = "url(/static/91acbc73057517.5bfd2266869a1.jpg)"
        document.querySelector("h6").innerHTML = "dark"
        filters.style.backgroundColor = "hsl(235, 24%, 19%)"
        tasks.style.backgroundColor = "hsl(235, 24%, 19%)"
        tasks.style.color = "hsl(0, 0%, 73%)"
        todo.style.backgroundColor = "hsl(235, 24%, 19%)"
        add.style.backgroundColor = "hsl(235, 24%, 19%)"

        counter++
        localStorage.setItem('counter', counter)
    }
    else
    {
        theme.style.backgroundImage = "url(/static/light.png)"
        document.querySelector("h6").innerHTML = "light"
        filters.style.backgroundColor = "white"
        tasks.style.backgroundColor = "white"
        tasks.style.color = "hsl(0, 0%, 26%)"
        todo.style.backgroundColor = "white"
        add.style.backgroundColor = "white"
        counter++
        localStorage.setItem('counter', counter)
    }
}

function keep_theme()
{
    theme = document.getElementById("main")

    if (localStorage.getItem('counter') % 2 == 1)
    {   
        theme = document.getElementById("main")
        filters = document.getElementById("theme")
        tasks = document.getElementById("theme1")
        todo = document.getElementById("todo-input")
        add = document.getElementById("add")

        theme.style.backgroundImage = "url(/static/light.png)"
        filters.style.backgroundColor = "white"
        tasks.style.backgroundColor = "white"
        tasks.style.color = "hsl(0, 0%, 26%)"
        todo.style.backgroundColor = "white"
        add.style.backgroundColor = "white"

        
    }
    else
    {
        theme = document.getElementById("main")
        filters = document.getElementById("theme")
        tasks = document.getElementById("theme1")
        todo = document.getElementById("todo-input")
        add = document.getElementById("add")

        theme.style.backgroundImage = "url(/static/91acbc73057517.5bfd2266869a1.jpg)"
        filters.style.backgroundColor = "hsl(235, 24%, 19%)"
        tasks.style.backgroundColor = "hsl(235, 24%, 19%)"
        tasks.style.color = "hsl(0, 0%, 73%)"
        todo.style.backgroundColor = "hsl(235, 24%, 19%)"
        add.style.backgroundColor = "hsl(235, 24%, 19%)"

    }
 
}

