{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNS-Bold;\f1\fnil\fcharset0 .SFNS-Regular;\f2\fswiss\fcharset0 Helvetica;
\f3\fmodern\fcharset0 Courier;\f4\froman\fcharset0 TimesNewRomanPSMT;\f5\fnil\fcharset0 .SFNS-RegularItalic;
\f6\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;}
{\colortbl;\red255\green255\blue255;\red14\green14\blue14;\red0\green0\blue0;\red111\green90\blue30;
\red20\green0\blue196;\red181\green0\blue19;\red13\green100\blue1;}
{\*\expandedcolortbl;;\cssrgb\c6700\c6700\c6700;\csgray\c0;\cssrgb\c51373\c42353\c15686;
\cssrgb\c10980\c0\c81176;\cssrgb\c76863\c10196\c8627;\cssrgb\c0\c45490\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37500\viewh17940\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs44 \cf2 Backend to Frontend Data Specification
\f1\b0\fs28 \
\
This document outlines the structure and content of the data sent from the backend to the frontend after processing an image. The data is in JSON format and contains product recommendations based on the analysis.
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Data Structure
\f1\b0\fs28 \
\
The JSON object returned by the backend has the following structure:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f3\fs28 \cf3 \{\
  \cf4 "recommendations"\cf3 : [\
    \{\
      \cf4 "skuID"\cf3 : <Integer>,\
      \cf4 "brandName"\cf3 : <String>,\
      \cf4 "displayName"\cf3 : <String>,\
      \cf4 "color_description"\cf3 : <String>,\
      \cf4 "price_value"\cf3 : <Float>,\
      \cf4 "Rating"\cf3 : <Integer>,\
      \cf4 "reviews"\cf3 : <Integer>,\
      \cf4 "recommendation_score"\cf3 : <Float>,\
      \cf4 "lipstick_image_base64"\cf3 : <String>\
    \},\
    ...\
  ]\
\}
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30 \cf2 Field Descriptions
\f1\b0\fs28 \
\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	
\f0\b recommendations
\f1\b0 : An array of product recommendation objects.\
\
Each recommendation object contains the following fields:\
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	1.	
\f0\b skuID
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : Integer\

\f5\i Description
\f1\i0 : The unique identifier for the product.\

\f5\i Example
\f1\i0 : 
\f6 2490274
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	2.	
\f0\b brandName
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : String\

\f5\i Description
\f1\i0 : The brand of the product.\

\f5\i Example
\f1\i0 : 
\f6 "TOM FORD"
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	3.	
\f0\b displayName
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : String\

\f5\i Description
\f1\i0 : The product\'92s display name.\

\f5\i Example
\f1\i0 : 
\f6 "Gloss Luxe Lip Gloss"
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	4.	
\f0\b color_description
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : String\

\f5\i Description
\f1\i0 : A description of the product\'92s color.\

\f5\i Example
\f1\i0 : 
\f6 "22 Sunrise Pink rosey nude"
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	5.	
\f0\b price_value
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : Float\

\f5\i Description
\f1\i0 : The price of the product.\

\f5\i Example
\f1\i0 : 
\f6 62.0
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	6.	
\f0\b Rating
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : Integer\

\f5\i Description
\f1\i0 : The product\'92s rating out of 5.\

\f5\i Example
\f1\i0 : 
\f6 5
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	7.	
\f0\b reviews
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : Integer\

\f5\i Description
\f1\i0 : The number of reviews the product has received.\

\f5\i Example
\f1\i0 : 
\f6 2322
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	8.	
\f0\b recommendation_score
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : Float\

\f5\i Description
\f1\i0 : The score assigned by the recommendation algorithm.\

\f5\i Example
\f1\i0 : 
\f6 103.73
\f1 \
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f4 \cf2 	9.	
\f0\b lipstick_image_base64
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\i \cf2 Type
\f1\i0 : String\

\f5\i Description
\f1\i0 : A Base64-encoded string of the product image.\

\f5\i Example
\f1\i0 : 
\f6 "/9j/4QRaRXhpZgAASUkqAAgAAAAQAAABAwABAAAA..."
\f1  (truncated)
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Example
\f1\b0\fs28 \
\
An example of the data sent from the backend:
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f3\fs28 \cf3 \{\
  \cf4 "recommendations"\cf3 : [\
    \{\
      \cf4 "skuID"\cf3 : \cf5 2490274\cf3 ,\
      \cf4 "brandName"\cf3 : \cf6 "TOM FORD"\cf3 ,\
      \cf4 "displayName"\cf3 : \cf6 "Gloss Luxe Lip Gloss"\cf3 ,\
      \cf4 "color_description"\cf3 : \cf6 "22 Sunrise Pink rosey nude"\cf3 ,\
      \cf4 "price_value"\cf3 : \cf5 62.0\cf3 ,\
      \cf4 "Rating"\cf3 : \cf5 5\cf3 ,\
      \cf4 "reviews"\cf3 : \cf5 2322\cf3 ,\
      \cf4 "recommendation_score"\cf3 : \cf5 103.73\cf3 ,\
      \cf4 "lipstick_image_base64"\cf3 : \cf6 "/9j/4QRaRXhpZgAASUkqAAgAAAAQAAABAwABAAAA..."\cf3  \cf7 // Image data truncated\cf3 \
    \},\
    \{\
      \cf4 "skuID"\cf3 : \cf5 1234567\cf3 ,\
      \cf4 "brandName"\cf3 : \cf6 "Brand XYZ"\cf3 ,\
      \cf4 "displayName"\cf3 : \cf6 "Lip Color Shine"\cf3 ,\
      \cf4 "color_description"\cf3 : \cf6 "10 Coral Red"\cf3 ,\
      \cf4 "price_value"\cf3 : \cf5 45.0\cf3 ,\
      \cf4 "Rating"\cf3 : \cf5 4\cf3 ,\
      \cf4 "reviews"\cf3 : \cf5 1580\cf3 ,\
      \cf4 "recommendation_score"\cf3 : \cf5 98.5\cf3 ,\
      \cf4 "lipstick_image_base64"\cf3 : \cf6 "/9j/4AAQSkZJRgABAQAAAQABAAD/..."\cf3  \cf7 // Image data truncated\cf3 \
    \}\
    \cf7 // Additional recommendation objects...\cf3 \
  ]\
\}
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs28 \cf2 Note
\f1\b0 : The 
\f6 lipstick_image_base64
\f1  field contains a Base64-encoded string representing the product image. For brevity, the actual string is truncated in this example.
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Usage
\f1\b0\fs28 \
\
The frontend application can parse this JSON data to display product recommendations, including images, prices, and ratings, to the user.
\f2\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 You can copy and paste this content into a Word document to create the README file.\
\

\f0\b\fs44 Short Summary
\f1\b0\fs28 \
\
The assistant has reformatted the previous response into a format suitable for a Word document, providing a detailed description of the data structure, field descriptions, examples, and usage, as requested by the user.}