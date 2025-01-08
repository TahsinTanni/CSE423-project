'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_APPLE_fence'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_APPLE_fence',error_checker=_errors._error_checker)
GL_DRAW_PIXELS_APPLE=_C('GL_DRAW_PIXELS_APPLE',0x8A0A)
GL_FENCE_APPLE=_C('GL_FENCE_APPLE',0x8A0B)
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteFencesAPPLE(n,fences):pass
@_f
@_p.types(None,_cs.GLuint)
def glFinishFenceAPPLE(fence):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glFinishObjectAPPLE(object,name):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFencesAPPLE(n,fences):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsFenceAPPLE(fence):pass
@_f
@_p.types(None,_cs.GLuint)
def glSetFenceAPPLE(fence):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glTestFenceAPPLE(fence):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glTestObjectAPPLE(object,name):pass
