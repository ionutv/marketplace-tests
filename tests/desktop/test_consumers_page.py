#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest

from unittestzero import Assert

from pages.desktop.consumer_pages.home import Home


class TestConsumerPage:

    @pytest.mark.nondestructive
    def test_that_verifies_the_most_popular_section(self, mozwebqa):
        '''https://www.pivotaltracker.com/projects/477093 ID:31913803'''

        home_page = Home(mozwebqa)
        home_page.go_to_homepage()

        Assert.true(home_page.is_the_current_page)

        # Check if the most popular section title is visible
        Assert.true(home_page.is_most_popular_section_title_visible)

        # Check if the most popular section is visible and contains applications
        Assert.true(home_page.is_most_popular_section_visible)
        for element in home_page.popular_section_elements_list:
            if element in home_page.popular_section_elements_list[:-1]:
                Assert.true(element.is_displayed())
            else:
                Assert.false(home_page.popular_section_elements_list[-1].is_displayed())

    @pytest.mark.nondestructive
    def test_that_verifies_featured_application_section(self, mozwebqa):
        '''https://www.pivotaltracker.com/projects/477093 ID:31913881'''

        home_page = Home(mozwebqa)
        home_page.go_to_homepage()

        Assert.true(home_page.is_the_current_page)

        # Check if featured application section title is visible
        Assert.true(home_page.is_featured_section_title_visible)

        # Check if featured section is visible and contains applications
        Assert.true(home_page.is_featured_section_visible)
        Assert.equal(home_page.featured_section_elements_count, 3)

    @pytest.mark.nondestructive
    def test_that_verifies_that_navigation_menu_is_available_and_the_links_work(self, mozwebqa):
        ''' https://www.pivotaltracker.com/projects/477093#!/stories/31913951'''

        home_page = Home(mozwebqa)
        home_page.go_to_homepage()

        Assert.true(home_page.is_the_current_page)

        # Check Home link
        home_page.header.navigation_menu.flyout_item('Home').click()
        Assert.true(home_page.is_the_current_page)

        # Check Popular link
        popular = home_page.header.navigation_menu.flyout_item('Popular').click()

        # Check page title
        Assert.true(popular.is_by_popularity_title_visible)
        Assert.equal(popular.title, 'By Popularity')

        # Check page breadcrumbs
        Assert.equal('Home', popular.breadcrumbs[0].text)
        Assert.equal('Apps', popular.breadcrumbs[1].text)
        Assert.equal('By Popularity', popular.breadcrumbs[2].text)

        # Check sorter header region
        Assert.true(popular.is_sorter_header_visible)
        Assert.equal('Weekly Downloads', popular.sorted_by)

        # Check Top Free link
        top_free = home_page.header.navigation_menu.flyout_item('Top Free').click()

        # Check page breadcrumbs
        Assert.equal('Home', top_free.breadcrumbs[0].text)
        Assert.equal('Apps', top_free.breadcrumbs[1].text)
        Assert.equal('Top Free', top_free.breadcrumbs[2].text)

        # Check sorter header region
        Assert.true(top_free.is_sorter_header_visible)
        Assert.equal('Weekly Downloads', top_free.sorted_by)

        # Check applied filters
        Assert.equal('Free Only', top_free.applied_filters)

        # Check Top Paid link
        top_paid = home_page.header.navigation_menu.flyout_item('Top Paid').click()

        # Check page breadcrumbs
        Assert.equal('Home', top_paid.breadcrumbs[0].text)
        Assert.equal('Apps', top_paid.breadcrumbs[1].text)
        Assert.equal('Top Paid', top_paid.breadcrumbs[2].text)

        # Check sorter header region
        Assert.true(top_paid.is_sorter_header_visible)
        Assert.equal('Weekly Downloads', top_paid.sorted_by)

        # Check applied filters
        Assert.equal('Premium Only', top_paid.applied_filters)

        # Check Categories link
        cat = home_page.header.navigation_menu.flyout_item('Categories').click()

        # Check page title
        Assert.equal('Apps | Mozilla Marketplace', cat.page_title)

        # Check the breadcrumbs
        Assert.equal('Home', cat.breadcrumbs[0].text)
        Assert.equal('Apps', cat.breadcrumbs[1].text)

        # Check all categories section
        Assert.true(cat.is_all_categories_title_visible)
        Assert.equal('All categories', cat.all_categories_title_text)
        Assert.equal(cat.all_categories_element_count, 15)
