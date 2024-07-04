/**
   JoystickShield - Arduino Library for JoystickShield (http://hardwarefun.com/projects/joystick-shield)

   Copyright 2011  Sudar Muthu  (email : sudar@sudarmuthu.com)

 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <sudar@sudarmuthu.com> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer or coffee in return - Sudar
 * ----------------------------------------------------------------------------
 * 2014 edit by Markus Mücke, muecke.ma(a)gmail.com
 * Changes for JoysikShield V1.2
 * added a function to read the amplitude of the joystick
 * added a auto calibrate function for 3.3V and 5V mode
 *
 * Added functions:
 *  Functions for F and E Button
 *  Calibrate Joystick
 *  xAmplitude
 *  yAmplitude
 */

/**
 * Before running this example, stack the JoystickShield on top of Arduino board
 *
 */

#include <JoystickShield.h> // include JoystickShield Library

bool A_Press=false;
bool B_Press=false;
bool C_Press=false;
bool D_Press=false;
bool F_Press=false;
bool E_Press=false;
bool K_Press=false;
bool e=false;

JoystickShield joystickShield; // create an instance of JoystickShield object

void setup() {
    Serial.begin(9600);
  
    delay(100);
    // new calibration function
    joystickShield.calibrateJoystick();
    
  // predefined Joystick to Pins 0 and 1.
  // Change it if you are using a different shield
  // setJoystickPins(0, 1);
  
  // predefined buttons to the following pins.
  // change it if you are using a different shield.
  // setButtonPins(pinJoystickButton, pinUp, pinRight, pinDown, pinLeft, pinF, pinE);
  // to deactivate a button use a pin outside of the range of the arduino e.g. 255, but not above
  // setButtonPins(8, 2, 3, 4, 5, 7, 6);
}

void loop() {
  joystickShield.processEvents(); // process events

  if (joystickShield.isJoystickButton()) {
    if (not K_Press){
      K_Press=true;
     Serial.println("K") ;
      }
  }

  if (joystickShield.isUpButton()) {
    if (not A_Press){
    A_Press=true;
     Serial.println("A") ;}
  }

  if (joystickShield.isRightButton()) {
    if (not B_Press){
  
    B_Press=true;
     Serial.println("B") ;}
  }

  if (joystickShield.isDownButton()) {
    if (not C_Press){
 
    C_Press=true;
     Serial.println("C") ;}
  }

  if (joystickShield.isLeftButton()) {
    if (not D_Press){
  
    D_Press=true;
     Serial.println("D") ;}
  }

  // new eventfunctions
  if (joystickShield.isFButton()) {
    if (not e){
    e=true;
    E_Press=true;
     Serial.println("F_") ;}
  }

  if (joystickShield.isEButton()) {
    if (not F_Press){
    
    F_Press=true;
     Serial.println("E") ;}
  }  
  
  if (not joystickShield.isJoystickButton()) {
    if (K_Press){
      K_Press=false;
      }
  }

  if (not joystickShield.isUpButton()) {
    if (A_Press){
    A_Press=false;}
  }

  if (not joystickShield.isRightButton()) {
    if (B_Press){
  
    B_Press=false;}
  }

  if (not joystickShield.isDownButton()) {
    if (C_Press){
 
    C_Press=false;}
  }

  if (not joystickShield.isLeftButton()) {
    if (D_Press){
  
    D_Press=false;}
  }

  // new eventfunctions
  if (not joystickShield.isFButton()) {
    if (E_Press){
    E_Press=false;  
    e=false;
    Serial.println("F-");}
  }

  if (not joystickShield.isEButton()) {
    if (F_Press){
  
    F_Press=false;}
  }
  // new position functions
  Serial.print("x"); Serial.print(joystickShield.xAmplitude());Serial.print("y");Serial.println(joystickShield.yAmplitude());
  delay(30);
}
