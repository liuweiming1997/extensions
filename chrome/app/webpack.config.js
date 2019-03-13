const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  entry: path.join(__dirname, "./main.js"),
  output: {
    path: path.join(__dirname, "build"),
    filename: "main.js"
  },
  devServer: {
    contentBase: path.join(__dirname, 'build'),
    compress: true,
    port: 3000
  },
  module: {
    rules: [{
      test: /(\.jsx|\.js)$/,
      use: {
        loader: "babel-loader",
        options: { 
          presets:['react']
        }
      },
      exclude: /node_modules/
    }, {
      test: /\.css$/,
      use: [{
        loader: "style-loader"
      }, {
        loader: "css-loader"
      }, {
        loader: "postcss-loader"
      }]
    }]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.join(__dirname, "main.html")
    })
  ]
}
