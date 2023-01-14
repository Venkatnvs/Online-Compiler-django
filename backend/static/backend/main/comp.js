let editor;
window.onload = function() {
    ace.require("ace/ext/language_tools");
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/idle_fingers");
    // editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setValue(python_base,-1);
    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true
    });
    editor.setFontSize(14);
}
php_base = `<?php
    echo "Hello, World!";
?>`;
js_base = `console.log("Hello, World!");`;
python_base = `print("Hello, World!")`;

c_base = `#include <stdio.h>

int main()
{
    printf("Hello, World!");
    return 0;
}`;
cpp_base = `#include <iostream>

int main()
{
    std::cout << "Hello, World!";
    return 0;
}`;

function sel_language() {
    let lan = $("#language").val();
    
    if(lan == 'c' || lan == 'cpp')
    {
        editor.session.setMode("ace/mode/c_cpp");
        if (lan=='c'){
            editor.setValue(c_base,-1);
            $(".file_name").text("main.c");
        }
        else{
            editor.setValue(cpp_base,-1);
            $(".file_name").text("main.cpp");
        }
    }
    else if(lan == 'php')
    {
        editor.session.setMode("ace/mode/php");
        editor.setValue(php_base,-1);
        $(".file_name").text("main.php");
    }
    else if(lan == 'py')
    {
        editor.session.setMode("ace/mode/python");
        editor.setValue(python_base,-1);
        $(".file_name").text("main.py");
    }
    else if(lan == 'js')
    {
        editor.session.setMode("ace/mode/javascript");
        editor.setValue(js_base,-1);
        $(".file_name").text("main.js");

    }
}
