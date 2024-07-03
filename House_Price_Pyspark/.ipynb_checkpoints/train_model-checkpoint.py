#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, explained_variance_score
from flask import Flask, jsonify

# Load data
df_hn = pd.read_csv('ha_noi_data.csv')
df_hcm = pd.read_csv('hcm_data.csv')
df_dn = pd.read_csv('dn_data.csv')

# Combine data
total_df = pd.concat([df_hn, df_hcm, df_dn], ignore_index=True)
total_df.to_csv('data.csv', encoding="utf-8-sig", index=False)
df_raw = pd.read_csv('data.csv')

# Data cleaning
df_raw = df_raw.drop(columns=['pty_characteristics','price_million_per_m2','shop_alias','date' ,'shop.alias', 'shop.status', 'shop.name', 'shop.address', 'shop.profileImageUrl', 'shop.createdDate', 'shop.modifiedDate', 'shop.urls', 'shop.shopsCategoriesRelationships', 'ad_id', 'list_id',  'account_id', 'account_oid', 'account_name', 'image', 'webp_image', 'videos', 'number_of_images', 'avatar', 'seller_info.full_name', 'seller_info.avatar', 'seller_info.sold_ads', 'seller_info.live_ads', 'has_video', 'company_logo', 'special_display_images', 'special_display', 'state', 'land_feature', 'street_id', 'size_unit', 'property_back_condition', 'property_road_condition', 'unitnumber_display', 'projectimages', 'project_oid', 'projectid', 'orig_list_time', 'streetnumber_display', 'ad_labels', 'label_campaigns', 'pty_jupiter', 'zero_deposit', 'escrow_can_deposit', 'protection_entitlement', 'owner', 'phone_hidden', 'contain_videos', 'type', 'params', 'address', 'location', 'longitude', 'latitude', 'company_ad', 'category', 'area', 'region','body', 'region_v2', 'area_v2', 'ward'], axis=1)

df_raw.drop(columns=['list_time','subject','price_string','ward_name','street_name'], inplace=True)

df_raw.rename(columns={
    'subject': 'TenBds',
    'category_name':'TheLoai',
    'area_name':'Huyen',
    'region_name':'Tinh',
    'price':'Gia',
    'rooms':'TongSoPhong',
    'property_legal_document':'GiayTo',
    'ward_name':'Phuong/Xa',
    'price_million_per_m2':'Gia/m2',
    'house_type':'LoaiHinhNhaO',
    'land_type':'LoaiHinhDat',
    'width':'ChieuNgang',
    'length':'ChieuDai',
    'toilets':'PhongVeSinh',
    'floors':'SoTang',
    'furnishing_sell':'NoiThat',
    'living_size':'DienTichSuDung',
    'commercial_type':'LoaiHinhVanPhong',
    'detail_address':'TenDuongCuThe',
    'direction':'HuongCuaChinh',
    'apartment_type':'LoaiHinhCanHo',
    'property_status':'TinhTrangBds',
    'street_number':'SoDuong',
    'block': 'TenPhanKhu/Lo/Block/Thap',
    'floornumber':'TangSo',
    'balconydirection':'HuongBanCong',
    'unitnumber':'MaLo',
    'apartment_feature':'DacDiemCanHoChungCu',
    'size':'DienTich(m2)',
    'street_name':'TenDuong'
}, inplace=True)

# Replace values
replacements = {
    'GiayTo': {1.0: 'Đã có sổ', 2.0: 'Đang chờ sổ', 3.0: 'Giấy tờ khác', 4.0: 'Hợp đồng đặt cọc', 5.0: 'Sổ chung', 6.0: 'Sổ hồng riêng'},
    'LoaiHinhNhaO': {1.0: 'Nhà mặt phố, mặt tiền', 2.0: 'Nhà ngõ, hẻm', 3.0: 'Nhà phố liền kề', 4.0: 'Nhà biệt thự'},
    'NoiThat': {1.0: 'Noi That cao cấp', 2.0: 'Noi That đầy đủ', 3.0: 'Hoàn thiện cơ bản', 4.0: 'Bàn giao thô'},
    'LoaiHinhVanPhong': {1.0: 'Shophouse', 2.0: 'Officetel', 3.0: 'Văn phòng', 4.0: 'Mặt bằng kinh doanh'},
    'HuongCuaChinh': {1.0: 'Đông', 2.0: 'Tây', 3.0: 'Nam', 4.0: 'Bắc', 5.0: 'Đông Bắc', 6.0: 'Đông Nam', 7.0: 'Tây Bắc', 8.0: 'Tây Nam'},
    'HuongBanCong': {1.0: 'Đông', 2.0: 'Tây', 3.0: 'Nam', 4.0: 'Bắc', 5.0: 'Đông Bắc', 6.0: 'Đông Nam', 7.0: 'Tây Bắc', 8.0: 'Tây Nam'},
    'LoaiHinhCanHo': {1.0: 'Chung cư', 2.0: 'Căn hộ dịch vụ, mini', 3.0: 'Duplex', 4.0: 'Penthouse', 5.0: 'Tập thể, cư xá', 6.0: 'Officetel'},
    'TinhTrangBds': {1.0: 'Chưa bàn giao', 2.0: 'Đã bàn giao'},
    'LoaiHinhDat': {1.0: 'Đất thổ cư', 2.0: 'Đất nền dự án', 3.0: 'Đất nông nghiệp', 4.0: 'Đất công nghiệp'},
    'DacDiemCanHoChungCu': {1.0: 'Căn góc'}
}

for col, replace_dict in replacements.items():
    df_raw[col].replace(replace_dict, inplace=True)

# Check the percentage of null values and drop columns with more than 51% null values
perce_null = df_raw.isna().sum() * 100 / df_raw.shape[0]
df2 = df_raw.drop(columns=perce_null[perce_null.values > 51].index)

# Fill null values for categorical variables with mode
for column in ['Huyen', 'GiayTo', 'LoaiHinhNhaO']:
    df2[column].fillna(value=df2[column].mode()[0], inplace=True)

# Handling outliers
q3_gia = df2['Gia'].quantile(0.98)
df2 = df2[(df2['Gia'] < q3_gia)]

q3_dientich = df2['DienTich(m2)'].quantile(0.99)
df2 = df2[df2['DienTich(m2)'] <= q3_dientich]

q3_chieungang = df2['ChieuNgang'].quantile(0.99)
df2 = df2[df2['ChieuNgang'] <= q3_chieungang]

q3_chieudai = df2['ChieuDai'].quantile(0.99)
df2 = df2[df2['ChieuDai'] <= q3_chieudai]

# Fill missing values with mean for numerical variables
for column in ['TongSoPhong', 'ChieuNgang', 'ChieuDai', 'PhongVeSinh', 'DienTich(m2)']:
    df2[column].fillna(value=df2[column].mean(), inplace=True)

# Feature transformations
df3 = df2.copy()
df_x = df3.drop(columns=['Gia'])
df_y = df3['Gia']

# Log transform for skewed features
skew_df = pd.DataFrame(df_x.select_dtypes(np.number).columns, columns=['Feature'])
skew_df['skew'] = skew_df['Feature'].apply(lambda x: scipy.stats.skew(df_x[x]))
skew_df['abs_skew'] = skew_df['skew'].apply(lambda x: abs(x))
skew_df['skewed'] = skew_df['abs_skew'].apply(lambda x: True if x > 0.5 else False)

for feature in skew_df[skew_df['skewed'] == True]['Feature']:
    df_x[feature] = df_x[feature].apply(lambda x: np.log(x))

# Encode categoricals
df4 = pd.get_dummies(data=df_x).astype(float)

# Scaling
scalar = StandardScaler()
data_preprocessing = scalar.fit_transform(df4)
df5 = pd.DataFrame(data=data_preprocessing, index=df4.index, columns=df4.columns)

# Log transform the target variable
k = df_y.apply(lambda x: np.log(x))
sns.displot(data=k, kde=True)

# Model training and testing
x_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(df5, k, test_size=0.2, random_state=105)
model = LinearRegression()
model.fit(x_train_lr, y_train_lr)
y_predictlr = model.predict(X_test_lr)

# Print model performance
print("R2 Score:", r2_score(y_test_lr, y_predictlr))
print("Explained Variance Score:", explained_variance_score(y_test_lr, y_predictlr))
# Save metrics to a file
with open("metrics.json", "w") as f:
    json.dump({"R2 Score": r2, "Explained Variance Score": explained_variance}, f)

# Flask app to serve results
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to the Model Performance API!"

# @app.route('/metrics', methods=['GET'])
# def metrics():
#     with open("metrics.json", "r") as f:
#         metrics = json.load(f)
#     return jsonify(metrics)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)