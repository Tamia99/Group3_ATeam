module.exports = {
    assetsDir: 'static',
    publicPath: process.env.NODE_ENV === "production" ? "./" : "/",
    devServer: {
        proxy: 'http://localhost:5000/',
        // proxy: 'http://localhost:8080/'
        // contentBase:path.join(_dirname,'src')
    }
}