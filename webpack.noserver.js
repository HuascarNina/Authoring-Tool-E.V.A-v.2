let webpack = require('webpack');
const merge = require('webpack-merge');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');
const common = require('./webpack.common.js');
let path = require('path');

module.exports = merge.smart(common, {
    entry: {
        'app': [
            'bootstrap-loader',
            './index.jsx',
        ],
        'visor': path.join(__dirname, '/_visor/containers/VisorApp.jsx'),
    },
    output: {
        path: path.join(__dirname, '/doc/dist/demo'),
        publicPath: '/', // Genera urls para imagenes
        filename: '[name]-bundle.min.js',
    },
    devtool: 'cheap-module-source-map',
    plugins: [
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.optimize.ModuleConcatenationPlugin(),

        new webpack.DefinePlugin({
            'process.env': {
                'NODE_ENV': JSON.stringify('production'),
                'DOC': JSON.stringify('doc'),
            },
        }),
    ],
});