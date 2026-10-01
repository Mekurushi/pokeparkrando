use std::path::{Path, PathBuf};

use pokeparkrando_core::{Appkprk, ReadAppkprkError};

pub(in crate::patcher) struct PatchFileState {
    path: PathBuf,
    contents: Appkprk,
}

impl PatchFileState {
    pub(in crate::patcher) fn read(path: PathBuf) -> Result<Self, ReadAppkprkError> {
        let contents = Appkprk::read(&path)?;
        Ok(Self { path, contents })
    }

    pub(in crate::patcher) fn path(&self) -> &Path {
        &self.path
    }

    pub(in crate::patcher) fn contents(&self) -> &Appkprk {
        &self.contents
    }
}
