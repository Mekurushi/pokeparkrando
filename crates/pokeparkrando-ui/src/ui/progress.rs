#[expect(
    clippy::cast_precision_loss,
    reason = "progress bars only require approximates"
)]
pub(crate) fn progress_fraction(completed: u64, total: u64) -> f32 {
    if total == 0 {
        return 0.0;
    }

    completed.min(total) as f32 / total as f32
}
