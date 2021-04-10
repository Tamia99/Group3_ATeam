module.exports = {
    assetsDir: 'static',
    devServer: {
        proxy: 'http://localhost:5000/',
        // proxy: 'http://localhost:8080/'
        // contentBase:path.join(_dirname,'src')
    }
}