# -*- coding: utf-8 -*-

from datetime import timedelta
from openerp import models, fields, api, exceptions

# Clase Cilindros
class Cylinder(models.Model):
	_name = 'cylinders.cylinder'

	number = fields.Char(string="Number", required=True)
	active = fields.Boolean(default=True)
	available = fields.Boolean(default=True)

	gas_id = fields.Many2one(
		'cylinders.gas', 'gas_id', string="Gas Type")

	@api.multi
	def copy(self, default=None):
		default = dict(default or {})

		copied_count = self.search_count(
			[('number', '=like', u"Copy of {}%".format(self.number))])
		if not copied_count:
			new_number = u"Copy of {}".format(self.number)
		else:
			new_number = u"Copy of {} ({})".format(self.number, copied_count)

	default['number'] = new_number
	return super(Cylinder, self).copy(default)

	_sql_constraints = [
		('number_unique',
		 'UNIQUE(number)',
		 "The Number for the cylinder must be unique")
	]

# Clase tipos de gases
class GasType(models.Model):
	_name = 'cylinders.gastype'

	name = fields.Char(string="Gas" required = True)
	description = fields.Text()

	@api.multi
	def copy(self, default=None):
		default = dict(default or {})

		copied_count = self.search_count(
			[('name', '=like', u"Copy of {}%".format(self.name))])
		if not copied_count:
			new_name = u"Copy of {}".format(self.name)
		else:
			new_name = u"Copy of {} ({})".format(self.name, copied_count)

	default['name'] = new_name
	return super(GasType, self).copy(default)

	_sql_constraints = [
		('number_unique',
		 'UNIQUE(name)',
		 "The name of the gas must be unique")
	]

# Clase Remitos
class Remit(models.Model):
	_name = 'cylinders.remit'

	name = fields.Char(required=True)

# class Session(models.Model):
#     _name = 'openacademy.session'

#     name = fields.Char(required=True)
#     start_date = fields.Date(default=fields.Date.today)
#     duration = fields.Float(digits=(6, 2), help="Duration in days")
#     seats = fields.Integer(string="Number of seats")
#     active = fields.Boolean(default=True)
#     color = fields.Integer()

#     instructor_id = fields.Many2one('res.partner', string="Instructor",
#         domain=['|', ('instructor', '=', True),
#                      ('category_id.name', 'ilike', "Teacher")])
#     course_id = fields.Many2one('openacademy.course',
#         ondelete='cascade', string="Course", required=True)
#     attendee_ids = fields.Many2many('res.partner', string="Attendees")

#     taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
#     end_date = fields.Date(string="End Date", store=True,
#         compute='_get_end_date', inverse='_set_end_date')

#     hours = fields.Float(string="Duration in hours",
#                          compute='_get_hours', inverse='_set_hours')

#     attendees_count = fields.Integer(
#         string="Attendees count", compute='_get_attendees_count', store=True)

#     state = fields.Selection([
#         ('draft', "Draft"),
#         ('confirmed', "Confirmed"),
#         ('done', "Done"),
#     ])

#     @api.multi
#     def action_draft(self):
#         self.state = 'draft'

#     @api.multi
#     def action_confirm(self):
#         self.state = 'confirmed'

#     @api.multi
#     def action_done(self):
#         self.state = 'done'

#     @api.depends('seats', 'attendee_ids')
#     def _taken_seats(self):
#         for r in self:
#             if not r.seats:
#                 r.taken_seats = 0.0
#             else:
#                 r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

#     @api.depends('attendee_ids')
#     def _get_attendees_count(self):
#         for r in self:
#             r.attendees_count = len(r.attendee_ids)

#     @api.onchange('seats', 'attendee_ids')
#     def _verify_valid_seats(self):
#         if self.seats < 0:
#             return {
#                 'warning': {
#                     'title': "Incorrect 'seats' value",
#                     'message': "The number of available seats may not be negative",
#                 },
#             }
#         if self.seats < len(self.attendee_ids):
#             return {
#                 'warning': {
#                     'title': "Too many attendees",
#                     'message': "Increase seats or remove excess attendees",
#                 },
#             }

#     @api.depends('start_date', 'duration')
#     def _get_end_date(self):
#         for r in self:
#             if not (r.start_date and r.duration):
#                 r.end_date = r.start_date
#                 continue

#             # Add duration to start_date, but: Monday + 5 days = Saturday, so
#             # subtract one second to get on Friday instead
#             start = fields.Datetime.from_string(r.start_date)
#             duration = timedelta(days=r.duration, seconds=-1)
#             r.end_date = start + duration

#     def _set_end_date(self):
#         for r in self:
#             if not (r.start_date and r.end_date):
#                 continue

#             # Compute the difference between dates, but: Friday - Monday = 4 days,
#             # so add one day to get 5 days instead
#             start_date = fields.Datetime.from_string(r.start_date)
#             end_date = fields.Datetime.from_string(r.end_date)
#             r.duration = (end_date - start_date).days + 1

#     @api.depends('duration')
#     def _get_hours(self):
#         for r in self:
#             r.hours = r.duration * 24

#     def _set_hours(self):
#         for r in self:
#             r.duration = r.hours / 24

#     @api.constrains('instructor_id', 'attendee_ids')
#     def _check_instructor_not_in_attendees(self):
#         for r in self:
#             if r.instructor_id and r.instructor_id in r.attendee_ids:
#                 raise exceptions.ValidationError("A session's instructor can't be an attendee")
# # class openacademy(models.Model):
# #     _name = 'openacademy.openacademy'

# #     name = fields.Char()