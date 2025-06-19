// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
use tauri::{command, Manager};

fn main() {
  tauri::Builder::default()
    .setup(|app| {
      let _child = std::process::Command::new("python")
        .arg("../../backend/app.py")
        .spawn()
        .expect("Failed to start backend");
      Ok(())
    })
    .run(tauri::generate_context!())
    .expect("error while running Tauri application");
}