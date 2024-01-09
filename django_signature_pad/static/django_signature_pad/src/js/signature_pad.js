/**
 * filename: signature_pad.js
 * 
 * This file initializes signature pad.
 * 
 * TODO: make this work with different libraries
 */

import '../css/signature_pad.css';
import SignaturePad from 'signature_pad' ;

// load the options data from django template variable (output from SignaturePadJSOptionsPath)
const options = JSON.parse(document.getElementById('signature_pad_options').textContent);
// console.log('options contain', options);


/**
 * function to debounce the operation for t seconds
 *  before executing the function
 * 
 * see https://stackoverflow.com/questions/45905160/javascript-on-window-resize-end
 */
function debounce(func, t=100){
  let timer;
  return function( event ){
    if ( timer ) {
      clearTimeout( timer );
    }
    timer = setTimeout(func, t, event);
  };
}


/**
 * function to resize the canvas for signature pad
 * 
 * This function handles high DPI screens.
 * see https://github.com/szimek/signature_pad
 * 
 * If the screen is larger than 1024 x 768, resize screen.
 * Otherwise, keep default widget size
 * 
 * params:  canvas - the canvas for the signature pad
 *          pad - the signature pad object
 *          width - the reference width for the canvas (const)
 *          height - the reference height for the canvas (const)
 * 
 * postcondition: a resized canvas with nothing in it
 */
function resizeCanvas(canvas, pad, width, height) {
  const defaultWidgetWidth = 306;
  const defaultWidgetHeight = 156;

  if ( window.screen.width >= 1024 && window.screen.height >= 768 ) {
    // console.log('resizing');
    const ratio =  Math.max(window.devicePixelRatio || 1, 1);

    // console.log('before canvas width is', width);
    // console.log('before canvas width is', height);

    canvas.width = width * ratio;
    canvas.height = height * ratio;
    // console.log('ratio is', ratio);
    
    // console.log('after canvas width is', canvas.width);
    // console.log('after canvas height is,', canvas.height);
    canvas.getContext("2d").scale(ratio, ratio);
    pad.clear(); // otherwise isEmpty() might return incorrect value
  } else if ( canvas.width <= defaultWidgetWidth && canvas.height <= defaultWidgetHeight ) {
    canvas.width = defaultWidgetWidth;
    canvas.height = defaultWidgetHeight;
  }
}


/**
 * function to temporarily get the signature from the data field and show it on
 * the signature pad
 * 
 * params:  pad - the signature pad object
 *          dataField - the data field to store the data url
 * 
 * postcondition: the data url string is stored as a value in datafield
 */
function getSignatureDataURL(pad, dataField) {
  if ( !pad.isEmpty() ) { // if pad is not empty
    // console.log('set data to dataField');
    dataField.value = pad.toDataURL('image/svg+xml');
  } 
}


/**
 * function to temporarily store the signature as a data url on a data field
 * 
 * params:  pad - the signature pad object
 *          dataField - the data field to store the data url
 * 
 * postcondition: the data url string is displayed on the signature pad
 */
function showSignatureDataURL(pad, dataField) {
  if ( dataField && dataField.value ) {
    pad.fromDataURL(dataField.value);
  }
}


// add event listeners
document.addEventListener('DOMContentLoaded', () => {
  // select all signature pad canvases
  const signaturePadWrappers = document.getElementsByClassName('signaturePadWrapper');

  [...signaturePadWrappers].forEach(wrapper => {
    const signatureData = wrapper.querySelector('input[type="hidden"]'); // the hidden field
    const canvas = wrapper.querySelector('canvas.signaturePadCanvas');

    // console.log('canvas variable contains', canvas)
    const signaturePad = new SignaturePad(canvas, options);

    // store the default width and height
    const defaultCanvasWidth = canvas.offsetWidth;
    const defaultCanvasHeight = canvas.offsetHeight;

    resizeCanvas(canvas, signaturePad, defaultCanvasWidth, defaultCanvasHeight);
    showSignatureDataURL(signaturePad, signatureData);
    
    // if window resized, resize the canvas
    window.addEventListener('resize', () => { 
      resizeCanvas(canvas, signaturePad, defaultCanvasWidth, defaultCanvasHeight);
    } );
    
    // if save button exists and is pressed, set data
    wrapper.querySelector('input.signaturePadSave')?.addEventListener('click', () => {
      // console.log('save button is pressed');
      getSignatureDataURL(signaturePad, signatureData);
      // console.log('set data to dataField', signatureData.value);
    } );
    
    // if reset button exists and is pressed, reset the pad
    wrapper.querySelector('input.signaturePadReset')?.addEventListener('click', () => {
      // console.log('resetting the pad');
      signaturePad.clear()
    } );
  })
});
