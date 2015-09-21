from django.db import models

class VirtualServer(models.Model):
  name = models.CharField(max_length=256)
  protocol = models.CharField(max_length=8, default="TCP")
  lb_algo = models.CharField(max_length=8, default="rr")
  lb_kind = models.CharField(max_length=8, default="FNAT")
  syn_proxy = models.BooleanField(default=True)
  persist_timeout = models.IntegerField(default=0)
  health_check = models.CharField(max_length=8, default="TCP")
  health_check_path = models.CharField(max_length=256)
  rise = models.PositiveSmallIntegerField(default=2)
  fall = models.PositiveSmallIntegerField(default=3)
  delay_loop = models.PositiveSmallIntegerField(default=6)
  create_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = "virtual_server"

class LocalAddess(models.Model):
  ip = models.CharField(max_length=16)
  class Meta:
    db_table = "local_address"

class ListenAddress(models.Model):
  ip = models.CharField(max_length=16)
  port = models.IntegerField()
  vs_id = models.ForeignKey(VirtualServer)
  
  class Meta:
    db_table = "listen_address"

class RealServer(models.Model):
  ip = models.CharField(max_length=16)
  port = models.IntegerField()
  weight = models.PositiveSmallIntegerField()
  vs_id = models.ForeignKey(VirtualServer)

  class Meta:
    db_table = "real_server"
