let editor;
window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setFontSize(14);
}

function sel_language() {
    let lan = $("#language").val();
    
    if(lan == 'c' || lan == 'cpp')
    {
        editor.session.setMode("ace/mode/c_cpp");
    }
    else if(lan == 'php')
    {
        editor.session.setMode("ace/mode/php");
    }
    else if(lan == 'py')
    {
        editor.session.setMode("ace/mode/python");
    }
    else if(lan == 'js')
    {
        editor.session.setMode("ace/mode/javascript");
    }
}
