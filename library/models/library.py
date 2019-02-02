# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    """
    Book main model
    """
    _name = "library.book"
    name = fields.Char(string="Name", required=True)
    release_date = fields.Date(string="Release Date", )
    cover = fields.Selection(
        string="Cover",
        selection=[
                ('soft', 'Soft'),
                ('hard', 'Hard'),
        ],
    )
    isbn = fields.Char(string="ISBN", size=20)
    summary = fields.Text(string="Summary", )
    author_ids = fields.Many2many(
        string="Authors",
        comodel_name="res.partner",
        relation="library_book_author",
        column1="book_id",
        column2="partner_id",
        help="Authors.",
    )
