const express = require("express")
const app = express()

const { spawn } = require('child_process');

const PORT = process.env.PORT || 3000

app.use(express.json())
app.use(express.static("public"))

app.set("view engine", 'ejs')

app.get("/", (req, res) => {

    res.render('index')
})


app.post('/searchProduct', (req, res) => {


    const { productName } = req.body

    var oProdutoName = productName

    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['main.py', oProdutoName]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.json(dataToSend)
    });


    // console.log(productName)


})
app.listen(PORT, () => console.log("Server running at port: " + PORT))