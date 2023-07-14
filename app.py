import streamlit as st
from torrentp import TorrentDownloader

st.title("Torrent Downloader App")

# Torrent file download
st.header("Download Torrent File")
torrent_file_path = st.text_input("Enter the path to the torrent file:")
if st.button("Download Torrent File"):
    torrent_file = TorrentDownloader(torrent_file_path, '.')
    torrent_file.start_download()
    st.success("Torrent file downloaded successfully!")

# Magnet link download
st.header("Download from Magnet Link")
magnet_link = st.text_input("Enter the magnet link:")
if st.button("Download from Magnet Link"):
    torrent_file = TorrentDownloader(magnet_link, '.')
    torrent_file.start_download()
    st.success("Download started from Magnet Link!")

