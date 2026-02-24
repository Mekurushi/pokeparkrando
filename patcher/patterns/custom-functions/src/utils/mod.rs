use core::ops::{Deref, DerefMut};

pub mod char_writer;
pub mod console;
pub mod graphics;

pub fn simple_rng(rng: &mut u32) -> u32 {
    *rng = rng.wrapping_mul(1664525).wrapping_add(1013904223);
    *rng
}

#[repr(align(0x20))]
pub struct AlignedBuf<const SIZE: usize, T = u8> {
    pub buf: [T; SIZE],
}

impl<const SIZE: usize, T: Copy + Default> Default for AlignedBuf<SIZE, T> {
    fn default() -> Self {
        Self {
            buf: [T::default(); SIZE],
        }
    }
}

impl<const SIZE: usize, T> Deref for AlignedBuf<SIZE, T> {
    type Target = [T; SIZE];
    fn deref(&self) -> &Self::Target {
        &self.buf
    }
}

impl<const SIZE: usize, T> DerefMut for AlignedBuf<SIZE, T> {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.buf
    }
}