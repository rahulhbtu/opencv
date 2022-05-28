from typing import List, Any, Tuple

import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


def upload():
    Imagepath: None | list[str | bytes | Any] | Literal[""] | tuple[str, ...] | str=easygui.fileopenbox()
    cartoonify(Imagepath)