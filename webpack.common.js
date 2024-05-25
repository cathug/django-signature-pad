// webpack settings based on
// https://pascalw.me/blog/2020/04/19/webpack-django.html
// but updated to work with webpack 5


const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const path = require('path');

const config = {
  entry: {
    signature_pad: './django_signature_pad/src/js/signature_pad.js',
  },

  plugins: [
    new MiniCssExtractPlugin(),
  ],

  output: {
    filename: '[name].js', // No filename hashing, Django takes care of this
    path: path.resolve(__dirname, 'django_signature_pad', 'static'),
    // publicPath: 'static/', // Should match Django STATIC_URL
    chunkFilename: "[id]-[chunkhash].js", // DO have Webpack hash chunk filename, see below
    assetModuleFilename: 'images/[hash][ext][query]',
    clean: true,
  },

  module: {
    rules: [
      {
        test: /\.(scss)$/i,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: () => [
                  require('autoprefixer')
                ]
              }
            }
          }, 
        ],
      },
      {
        test: /\.(css)$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader',],
      },
    ],
  },

  // minify css and js files in production
  optimization: {
    minimizer: [
      // remove all comments from js files
      new TerserPlugin({
        terserOptions: {
          format: {
            comments: false,
          },
        },
        extractComments: false,
      }),
      new CssMinimizerPlugin(),
    ],
  },

};


module.exports = config;