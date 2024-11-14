import streamlit as st
from plotly.subplots import make_subplots
import plotly.express as px

def real_estate(total_df):
    st.sidebar.title("Chart Option")

    option = st.sidebar.selectbox("Choose Option (e.g. 마포구)"
                                  , ("강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구")
                                  , )
    
    radio = st.sidebar.radio("House Type", ["아파트", "단독다가구", "오피스텔", "연립다세대"])


    st.markdown("## 2024년 3분기 서울 부동산 차트 (~11/12) \n")
    filtered_df = total_df[total_df['CGG_NM'] == option]
    filtered_df = filtered_df[filtered_df['CTRT_DAY'].between("2024-09-01", "2024-11-12")]
    filtered_df = filtered_df[filtered_df['BLDG_USG'] == radio]
    result = filtered_df.groupby(['CTRT_DAY', 'BLDG_USG'])['THING_AMT'].count().reset_index().rename(columns = {'THING_AMT' : '거래건수'})

    result2 = filtered_df.groupby(['CTRT_DAY', 'BLDG_USG'])['THING_AMT'].agg('mean').reset_index()

    # Create subplots with 2 rows and 2 columns

    fig = make_subplots(rows=2,
                        cols=1,
                        shared_xaxes=True,
                        subplot_titles=('가구별 거래건수 추세', '가구당 평균 가격 추세'),
                        horizontal_spacing=0.15)

    # Add line graphs to the subplots
    fig.add_trace(px.line(result,
                          x='CTRT_DAY',
                          y='거래건수',
                          title="가구별 거래 건수 추세", markers=True).data[0], row=1, col=1)
    fig.add_trace(px.line(result2,
                          x='CTRT_DAY',
                          y='THING_AMT',
                          title="가구당 평균 가격 추세", markers=True).data[0], row=2, col=1)

    fig.update_xaxes(showticklabels=True, row=1, col=1)

    fig.update_yaxes(title_text="거래건수", row=1, col=1)

    y_values = [0, 100000, 200000, 300000, 400000, 500000]
    y_labels = ["0", "10", "20", "30", "40", "50"]

    fig.update_yaxes(title_text="평균 가격 (억)", tickvals=y_values, ticktext=y_labels, row=2, col=1)


    fig.update_layout(
        width=900,
        height=700,
        showlegend=True,
        template='plotly_white'
    )

    st.plotly_chart(fig)

