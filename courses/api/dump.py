class TglProsesAdmin(admin.ModelAdmin):
	list_display = ('tgl_proses',)



	def response_add(self, request, obj, post_url_continue=None):
		if not '_continue' in request.POST:
			date_today = obj.tgl_proses
			#list_penjualan = Penjualan.objects.all().exclude(lunas=True).exclude(status="Penjualan Tunai").exclude(cabang=5).exclude(cabang=6).exclude(cabang=7).exclude(cabang=8)
			list_penjualan = Penjualan.objects.filter(lunas=False, cabang__id__in=[1,2,3,4]).exclude(status="Penjualan Tunai").exclude(tgl_transaksi__isnull=True)
			get_list_latest_pembayaran = Pembayaran.objects.order_by('stok').distinct()

			for i in list_penjualan:
				exist_kp = KartuPiutang.objects.filter(stok=i)
				count_exist_kp = exist_kp.count()
				if count_exist_kp < 1:
					#Create Kartu Piutang
					if i.jangka_waktu != 0 or i.jangka_waktu!=None:
						saldo_piutang = i.saldo_piutang - i.cicilan_bulanan

						if i.jangka_waktu >=1 and i.jangka_waktu <=6:
							persen_bunga = 0.05435
						elif i.jangka_waktu >=7 and i.jangka_waktu <= 14:
							persen_bunga = 0.05578
						elif i.jangka_waktu >=15 and i.jangka_waktu <=18:
							persen_bunga = 0.05501
						elif i.jangka_waktu >=19 and i.jangka_waktu <=26:
							persen_bunga = 0.05385
						elif i.jangka_waktu >=27 and i.jangka_waktu <=32:
							persen_bunga = 0.05267
						elif i.jangka_waktu >=33 and i.jangka_waktu <=36:
							persen_bunga = 0.05155

						for x in range(1,i.jangka_waktu+1):

							list_kartu_piutang = KartuPiutang.objects.filter(stok=i)
							count_kp = list_kartu_piutang.count()

							if count_kp < 1:
								if i.jangka_waktu == x:

									new_kartu_piutang = KartuPiutang()
									if i.tgl_transaksi.day == 31:
										new_kartu_piutang.tgl_jatuh_tempo = i.tgl_transaksi + relativedelta(months=+1)
									else:
										new_kartu_piutang.tgl_jatuh_tempo = i.tgl_transaksi + relativedelta(months=+1)

									new_kartu_piutang.stok = i
									new_kartu_piutang.kartu_angsuran = x
									new_kartu_piutang.kartu_sisa_piutang = 0
									new_kartu_piutang.kartu_bunga = float(i.cicilan_bulanan) - float(i.s_p_pokok)
									new_kartu_piutang.kartu_pokok = float(i.s_p_pokok)
									new_kartu_piutang.kartu_sisa_sp_pokok = 0
									new_kartu_piutang.kartu_sisa_saldo_bunga = 0

									new_kartu_piutang.created_at = datetime.date.today()
									new_kartu_piutang.updated_at = datetime.date.today()
									new_kartu_piutang.save()


								else:
									new_kartu_piutang = KartuPiutang()
									if i.tgl_transaksi.day == 31:
										new_kartu_piutang.tgl_jatuh_tempo = i.tgl_transaksi + relativedelta(months=+1)
									else:
										new_kartu_piutang.tgl_jatuh_tempo = i.tgl_transaksi + relativedelta(months=+1)

									new_kartu_piutang.stok = i
									new_kartu_piutang.kartu_angsuran = x
									new_kartu_piutang.kartu_sisa_piutang = i.saldo_piutang-i.cicilan_bulanan
									new_kartu_piutang.kartu_bunga = float(persen_bunga)*float(i.s_p_pokok)
									new_kartu_piutang.kartu_pokok = i.cicilan_bulanan - new_kartu_piutang.kartu_bunga
									new_kartu_piutang.kartu_sisa_sp_pokok = float(i.s_p_pokok)-float(new_kartu_piutang.kartu_pokok)
									new_kartu_piutang.kartu_sisa_saldo_bunga = float(new_kartu_piutang.kartu_sisa_piutang) - float(new_kartu_piutang.kartu_sisa_sp_pokok)
									new_kartu_piutang.created_at = datetime.date.today()
									new_kartu_piutang.updated_at = datetime.date.today()
										#saldo_piutang-=i.cicilan_bulanan
										#harga_total -= float(new_kartu_piutang.kartu_pokok)
									new_kartu_piutang.save()

							elif count_kp >=1:
								if i.jangka_waktu == x:
									get_latest_kp = list_kartu_piutang.latest('kartu_angsuran')
									new_kartu_piutang = KartuPiutang()

									if get_latest_kp.tgl_jatuh_tempo.day ==28 and get_latest_kp.tgl_jatuh_tempo.month == 02:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + datetime.timedelta(days=31)
									elif get_latest_kp.tgl_jatuh_tempo.day == 30 and i.tgl_transaksi.day !=30:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + relativedelta(months=+1) + datetime.timedelta(days=1)
									else:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + relativedelta(months=+1)
									new_kartu_piutang.stok = i
									new_kartu_piutang.kartu_angsuran = x
									new_kartu_piutang.kartu_sisa_piutang = 0
									new_kartu_piutang.kartu_pokok = get_latest_kp.kartu_sisa_sp_pokok
									new_kartu_piutang.kartu_bunga = i.cicilan_bulanan - new_kartu_piutang.kartu_pokok
									new_kartu_piutang.kartu_sisa_sp_pokok = 0
									new_kartu_piutang.kartu_sisa_saldo_bunga = 0
									new_kartu_piutang.created_at = datetime.date.today()
									new_kartu_piutang.updated_at = datetime.date.today()
									new_kartu_piutang.save()



								else:
									get_latest_kp = list_kartu_piutang.latest('kartu_angsuran')
									new_kartu_piutang = KartuPiutang()
									if get_latest_kp.tgl_jatuh_tempo.day == 28 and get_latest_kp.tgl_jatuh_tempo.month == 02:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + datetime.timedelta(days=31)
									elif get_latest_kp.tgl_jatuh_tempo.day == 30 and i.tgl_transaksi.day !=30:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + relativedelta(months=+1) + datetime.timedelta(days=1)
									else:
										new_kartu_piutang.tgl_jatuh_tempo = get_latest_kp.tgl_jatuh_tempo + relativedelta(months=+1)
									new_kartu_piutang.stok = i
									new_kartu_piutang.kartu_angsuran = x
									new_kartu_piutang.kartu_sisa_piutang = get_latest_kp.kartu_sisa_piutang-i.cicilan_bulanan
									new_kartu_piutang.kartu_bunga = float(persen_bunga)*float(get_latest_kp.kartu_sisa_sp_pokok)
									new_kartu_piutang.kartu_pokok = i.cicilan_bulanan - new_kartu_piutang.kartu_bunga
									new_kartu_piutang.kartu_sisa_sp_pokok = float(get_latest_kp.kartu_sisa_sp_pokok)-float(new_kartu_piutang.kartu_pokok)
									new_kartu_piutang.kartu_sisa_saldo_bunga = float(new_kartu_piutang.kartu_sisa_piutang) - float(new_kartu_piutang.kartu_sisa_sp_pokok)
									new_kartu_piutang.created_at = datetime.date.today()
									new_kartu_piutang.updated_at = datetime.date.today()
									new_kartu_piutang.save()
									print new_kartu_piutang
				elif count_exist_kp >= 1:
					if i.tgl_transaksi.day < i.tgl_penjualan.day:
						if i.tgl_transaksi.day <= 28:
							for kp in exist_kp:
								#print kp.stok.cabang

								tgl_jatuh_tempo = str(kp.tgl_jatuh_tempo)
								tgl_jt_baru = str (i.tgl_transaksi)[8:10]
								kp.tgl_jatuh_tempo = datetime.datetime(kp.tgl_jatuh_tempo.year, kp.tgl_jatuh_tempo.month, int(tgl_jt_baru))
								print kp
								kp.save()
					else:
						pass



			#return HttpResponseRedirect('http://localhost:8000/report')
			#clean_up kwalitas
			Kwalitas.objects.all().delete()
			#Create Kualitas
			for penjualan in list_penjualan:

				get_payments = Pembayaran.objects.filter(stok=penjualan).exclude(tgl_pembayaran__gt=date_today)
				count_gp = get_payments.count()

				if count_gp >= 1:

					get_latest_payment = get_payments.latest('angsuran')
					try:
						get_kartu_piutang = get_latest_payment.kartu_piutang
					except ObjectDoesNotExist:
						get_kartu_piutang = None

					if get_kartu_piutang:
						#print get_kartu_piutang
						#Rubah Status Kwalitas
						delta = date_today - get_kartu_piutang.tgl_jatuh_tempo
						#delta = get_latest_payment.tgl_pembayaran - get_latest_payment.tgl_jatuh_tempo
						range_days = delta.days
						if range_days < 7:
							status="Lancar"
						elif range_days >=7  and range_days <= 45:
							status ="KurangLancar"
						elif range_days > 45 and range_days <= 135:
							status = "Diragukan"
						elif range_days > 135:
							status = "Macet"
						try:
							existing_kwalitas = Kwalitas.objects.get(penjualan=penjualan, kartu_piutang__kartu_angsuran=get_latest_payment.angsuran)

						except ObjectDoesNotExist:
							new_kwalitas = Kwalitas()
							new_kwalitas.penjualan=penjualan
							new_kwalitas.kartu_piutang=get_kartu_piutang
							new_kwalitas.jenis_kwalitas=status
							new_kwalitas.sisa_piutang = get_kartu_piutang.kartu_sisa_piutang
							new_kwalitas.sisa_pokok = get_kartu_piutang.kartu_sisa_sp_pokok
							new_kwalitas.sisa_bunga = get_kartu_piutang.kartu_sisa_saldo_bunga
							new_kwalitas.save()

							list_kwalitas = Kwalitas.objects.filter(penjualan=penjualan)
							if len(list_kwalitas) > 1:

								list_kwalitas[0].delete()
				elif count_gp == 0:
					#Untuk dinamis kwalitas
					if penjualan.tgl_transaksi <= date_today:
						try:
							get_kartu_piutang = KartuPiutang.objects.get(stok=penjualan, kartu_angsuran=1)
						except ObjectDoesNotExist:
							get_kartu_piutang = None
						if get_kartu_piutang:
							delta = date_today - get_kartu_piutang.tgl_jatuh_tempo
							#delta = get_latest_payment.tgl_pembayaran - get_latest_payment.tgl_jatuh_tempo
							range_days = delta.days
							if range_days < 7:
								status="Lancar"
							elif range_days >=7 and range_days <= 45:
								status ="KurangLancar"
							elif range_days > 45 and range_days <= 135:
								status = "Diragukan"
							elif range_days > 135:
								status = "Macet"
							try:
								existing_kwalitas = Kwalitas.objects.get(penjualan=penjualan)

							except ObjectDoesNotExist:
								new_kwalitas = Kwalitas()
								new_kwalitas.penjualan=penjualan
								new_kwalitas.kartu_piutang=get_kartu_piutang
								new_kwalitas.jenis_kwalitas=status
								new_kwalitas.sisa_piutang = penjualan.saldo_piutang
								new_kwalitas.sisa_pokok = penjualan.s_p_pokok
								new_kwalitas.sisa_bunga = penjualan.saldo_bunga
								new_kwalitas.save()

								list_kwalitas = Kwalitas.objects.filter(penjualan=penjualan)
								if len(list_kwalitas) > 1:

									list_kwalitas[0].delete()

			list_lunas_kwalitas = Kwalitas.objects.filter(penjualan__lunas=True)
			list_lunas_kwalitas.delete()
			list_kwalitas = Kwalitas.objects.all()

			total_piutang = 0

			#perbaiki rumus ini krna belum ada pembayaran jgn ambil dr KP

			for kwalitas in list_kwalitas:
				total_piutang += kwalitas.sisa_piutang

			for kwalitas in list_kwalitas:
				rounding = float(kwalitas.sisa_piutang/total_piutang)
				kwalitas.persentase = float(rounding)*100
				kwalitas.save()
			#return HttpResponseRedirect('http://localhost:8000/report')

			#Hitung Penyusutan Inventory
			inventories = Inventaris.objects.all()
			for inventaris in inventories:
				inventaris.tgl_jt = inventaris.tgl_pembelian + relativedelta(months=inventaris.lama_penyusutan)


				months = lambda a, b: abs((a.year - b.year)*12 + a.month - b.month)
				range_months = months(date_today,inventaris.tgl_pembelian)
				if range_months > inventaris.lama_penyusutan :
					inventaris.periode = inventaris.lama_penyusutan
					inventaris.kumulatif_penyusutan = inventaris.harga_pembelian
					inventaris.sisa_nilai = 0
				elif range_months < inventaris.lama_penyusutan:
					inventaris.periode = range_months
					inventaris.kumulatif_penyusutan = int(range_months) * int(inventaris.penyusutan_perbulan)
					inventaris.sisa_nilai = int(inventaris.harga_pembelian) - int(inventaris.kumulatif_penyusutan)
				inventaris.save()

			#Rubah Pot Bungan None = 0
# 			payments = Pembayaran.objects.all()
# 			for pembayaran in payments:
# 				if pembayaran.potongan_bunga == None:
# 					pembayaran.potongan_bunga = 0
# 				pembayaran.save()
			return HttpResponseRedirect('http://solved.pythonanywhere.com/report/Laporan-Kwalitas-Piutang/')

		else:
			return super(TglProsesAdmin, self).response_add(request, obj, post_url_continue)

admin.site.register(TglProses,TglProsesAdmin)