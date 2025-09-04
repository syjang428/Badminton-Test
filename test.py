# ------------------ (선택) Google Sheets 연동 가이드 ------------------
with st.expander("📗 Google Sheets 연동 (옵션)"):
    st.markdown(
        """
        **간단 가이드**
        1) 서비스 계정 JSON(`service_account.json`)을 앱 루트에 두세요.
        2) 스프레드시트 URL과 워크시트 이름을 `secrets.toml` 또는 사이드바 입력으로 설정하세요.
        3) 아래 예시 코드를 참고하여 `save_history`를 구글시트 추가 저장으로 확장할 수 있어요.

        ```python
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        def get_sheet(spreadsheet_url, worksheet_name):
            scope = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive",
            ]
            creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
            client = gspread.authorize(creds)
            sh = client.open_by_url(spreadsheet_url)
            return sh.worksheet(worksheet_name)

        # save_history 내부에서 df를 시트에 append
        # ws.append_rows(df.values.tolist())
        ```
        """
    )