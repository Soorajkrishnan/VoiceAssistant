function start() {
  let { PythonShell } = require("python-shell");
  var cwd = process.cwd();
  message = $(".message-input input").val();
  var options = {
    scriptPath: cwd+"/back-end/",
    pythonPath : '/usr/bin/python',
    args: [message]

  };
  var pyshell = PythonShell.run("ipc1.py", options, function(err) {
    if (err) throw err;
    console.log("finished");
    $("#mic").attr("src", "images/mic.png");
  });
  console.log(cwd+"/back-end/");
  pyshell.on("message", function(message) {
    console.log(message);
  });

  $("#mic").attr("src", "images/mic2.png");

  /*var options = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: ath.join(__dirname),
  };

  PythonShell.run('brain.py', options, function (err, textb) {
    if (err) throw err;
  });*/
}
