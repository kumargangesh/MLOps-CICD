import streamlit as sl

n = sl.number_input("enter value: ", value=1, step=1)

square = n**2
cube = n**3

sl.write(f"Square of {n} : {square}")
sl.write(f"Cube of {n} : {cube}")