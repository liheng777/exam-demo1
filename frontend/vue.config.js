const path = require('path')

function resolve(dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  lintOnSave: 'error',
  publicPath: process.env.NODE_ENV === 'production' ? './static/dist' : '/',
  filenameHashing: false,
  devServer: {
    proxy: 'http://127.0.0.1:8000',
    disableHostCheck: true,
    port: 8080
  },
  chainWebpack: (config) => {
    config.resolve.alias
      .set('@a', resolve('src/assets'))
      .set('@c', resolve('src/components'))
      .set('@s', resolve('src/service'))
    config.optimization.delete('splitChunks')
  }
}
