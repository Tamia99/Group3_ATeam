module.exports = {
    assetsDir: 'static',
    publicPath: process.env.NODE_ENV === "production" ? "./" : "/",
    devServer: {
        proxy: 'http://localhost:5000/',
        // proxy: 'http://localhost:8080/'
        // contentBase:path.join(_dirname,'src')
    },
    chainWebpack: config => {
        config.module
            .rule('scss')
            .use('px2rem-loader')
            .loader('px2rem-loader')
            .options({
             remUnit: 108,
             remPrecision: 8
            })
    }
}